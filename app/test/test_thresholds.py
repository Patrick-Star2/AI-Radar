
from app.tools.embedding import get_embedding
from app.tools.similarity import cosine_similarity
from app.experiments.embedding_eval.dataset import TEST_PAIRS


def calculate_metrics(y_true, y_pred):
    """计算分类评估指标"""

    tp = sum(
        1 for true, pred in zip(y_true, y_pred)
        if true == 1 and pred == 1
    )
    fp = sum(
        1 for true, pred in zip(y_true, y_pred)
        if true == 0 and pred == 1
    )
    fn = sum(
        1 for true, pred in zip(y_true, y_pred)
        if true == 1 and pred == 0
    )
    tn = sum(
        1 for true, pred in zip(y_true, y_pred)
        if true == 0 and pred == 0
    )

    total = len(y_true)

    accuracy = (tp + tn) / total if total else 0
    precision = tp / (tp + fp) if tp + fp else 0
    recall = tp / (tp + fn) if tp + fn else 0

    f1 = (
        2 * precision * recall / (precision + recall)
        if precision + recall else 0
    )

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "tp": tp,
        "fp": fp,
        "fn": fn,
        "tn": tn,
    }


def main():
    print("开始计算 Embedding 向量...")

    # 先计算所有搜索词的向量，避免重复调用 API
    embedding_cache = {}

    for pair in TEST_PAIRS:
        for query in (pair["query_a"], pair["query_b"]):
            if query not in embedding_cache:
                embedding_cache[query] = get_embedding(query)

    # 计算每组搜索词的相似度
    results = []

    for pair in TEST_PAIRS:
        similarity = cosine_similarity(
            embedding_cache[pair["query_a"]],
            embedding_cache[pair["query_b"]]
        )

        results.append({
            **pair,
            "similarity": similarity,
        })

    thresholds = [
        0.50, 0.55, 0.60, 0.65,
        0.70, 0.75, 0.80, 0.85, 0.90
    ]

    y_true = [item["label"] for item in results]

    print("\n========== 阈值评估结果 ==========")

    best_result = None

    for threshold in thresholds:
        y_pred = [
            1 if item["similarity"] >= threshold else 0
            for item in results
        ]

        metrics = calculate_metrics(y_true, y_pred)

        print(f"\n阈值：{threshold:.2f}")
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

        # 以 F1 作为当前实验的综合排序指标
        if (
            best_result is None
            or metrics["f1"] > best_result["f1"]
        ):
            best_result = {
                "threshold": threshold,
                **metrics,
            }

    # 输出错误判断，方便分析
    print("\n========== 错误判断分析 ==========")

    for threshold in thresholds:
        errors = []

        for item in results:
            predicted = (
                1 if item["similarity"] >= threshold else 0
            )

            if predicted != item["label"]:
                errors.append({
                    **item,
                    "predicted": predicted,
                })

        print(f"\n阈值 {threshold:.2f}：")

        if not errors:
            print("没有错误判断")
            continue

        for item in errors:
            print(
                f"相似度：{item['similarity']:.4f} | "
                f"人工标签：{item['label']} | "
                f"预测标签：{item['predicted']}"
            )
            print(f"A：{item['query_a']}")
            print(f"B：{item['query_b']}")

    print("\n========== 当前最佳阈值 ==========")
    print(f"阈值：{best_result['threshold']:.2f}")
    print(f"F1：{best_result['f1']:.4f}")
    print(f"准确率：{best_result['accuracy']:.2%}")


if __name__ == "__main__":
    main()
