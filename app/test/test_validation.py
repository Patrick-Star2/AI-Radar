
from app.tools.embedding import get_embedding
from app.tools.similarity import cosine_similarity
from app.test.test_thresholds import calculate_metrics
from app.experiments.embedding_eval.validation_dataset import VALIDATION_PAIRS


# 固定使用校准阶段选出的候选阈值
THRESHOLD = 0.80


def main():
    print("开始独立验证...")
    print(f"固定阈值：{THRESHOLD}")

    # 检查数据集
    if not VALIDATION_PAIRS:
        raise ValueError("验证数据集不能为空")

    positive_count = sum(
        1 for item in VALIDATION_PAIRS if item["label"] == 1
    )
    negative_count = sum(
        1 for item in VALIDATION_PAIRS if item["label"] == 0
    )

    print(f"验证样本总数：{len(VALIDATION_PAIRS)}")
    print(f"正样本：{positive_count}")
    print(f"负样本：{negative_count}")

    # 缓存 Embedding，避免重复调用 API
    embedding_cache = {}

    for pair in VALIDATION_PAIRS:
        for query in (pair["query_a"], pair["query_b"]):
            if query not in embedding_cache:
                embedding_cache[query] = get_embedding(query)

    # 计算相似度并进行判断
    results = []

    for pair in VALIDATION_PAIRS:
        similarity = cosine_similarity(
            embedding_cache[pair["query_a"]],
            embedding_cache[pair["query_b"]]
        )

        predicted = 1 if similarity >= THRESHOLD else 0

        results.append({
            **pair,
            "similarity": similarity,
            "predicted": predicted,
        })

    # 计算评估指标
    y_true = [item["label"] for item in results]
    y_pred = [item["predicted"] for item in results]

    metrics = calculate_metrics(y_true, y_pred)

    print("\n========== 独立验证结果 ==========")
    print(f"准确率：{metrics['accuracy']:.2%}")
    print(f"精确率：{metrics['precision']:.2%}")
    print(f"召回率：{metrics['recall']:.2%}")
    print(f"F1：{metrics['f1']:.4f}")

    print(
        f"TP={metrics['tp']} "
        f"FP={metrics['fp']} "
        f"FN={metrics['fn']} "
        f"TN={metrics['tn']}"
    )

    # 输出全部样本结果
    print("\n========== 样本判断详情 ==========")

    for index, item in enumerate(results, start=1):
        status = "正确" if item["label"] == item["predicted"] else "错误"

        print(f"\n第 {index} 组 | {status}")
        print(f"相似度：{item['similarity']:.4f}")
        print(f"人工标签：{item['label']}")
        print(f"预测标签：{item['predicted']}")
        print(f"A：{item['query_a']}")
        print(f"B：{item['query_b']}")

    # 汇总错误案例
    errors = [
        item for item in results
        if item["label"] != item["predicted"]
    ]

    print("\n========== 错误案例汇总 ==========")

    if not errors:
        print("没有错误判断")
    else:
        for item in errors:
            print(
                f"相似度：{item['similarity']:.4f} | "
                f"人工标签：{item['label']} | "
                f"预测标签：{item['predicted']}"
            )
            print(f"A：{item['query_a']}")
            print(f"B：{item['query_b']}")

    print("\n========== 验证完成 ==========")


if __name__ == "__main__":
    main()
