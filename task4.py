def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta):
    indent = ' ' * (3 * (3 - depth))  # Indent for clarity based on depth
    if depth == 0 or node_index >= len(values):
        print(f"{indent}Leaf node at index {node_index} with value {values[node_index]}")
        return values[node_index]

    if maximizing_player:
        max_eval = float('-inf')
        print(f"{indent}Max node {node_index}: start with alpha={alpha}, beta={beta}")
        for i in range(2):
            eval = alpha_beta_pruning(depth - 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            print(f"{indent}Max node {node_index}: updated max_eval={max_eval}, alpha={alpha}")
            if beta <= alpha:
                print(f"{indent}Max node {node_index}: pruning branches with beta={beta} <= alpha={alpha}")
                break
        return max_eval
    else:
        min_eval = float('inf')
        print(f"{indent}Min node {node_index}: start with alpha={alpha}, beta={beta}")
        for i in range(2):
            eval = alpha_beta_pruning(depth - 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            print(f"{indent}Min node {node_index}: updated min_eval={min_eval}, beta={beta}")
            if beta <= alpha:
                print(f"{indent}Min node {node_index}: pruning branches with beta={beta} <= alpha={alpha}")
                break
        return min_eval

if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    depth = 3
    alpha = float('-inf')
    beta = float('inf')
    optimal_value = alpha_beta_pruning(depth, 0, True, values, alpha, beta)
    print(f"\nThe optimal value is: {optimal_value}")
