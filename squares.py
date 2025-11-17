import argparse
"""Computation of weighted average of squares.
计算平方的加权平均值。
"""


def average_of_squares(list_of_numbers, list_of_weights=None):
    """ 返回一组数的平方的加权平均值。
    
    默认情况下，所有值的权重相同，但可以通过参数 list_of_weights 来修改。
    
    示例：
    --------
    >>> average_of_squares([1, 2, 4]) # 默认权重均为 1
    7.0
    >>> average_of_squares([2, 4], [1, 0.5]) #括号后面是权重
    8.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length
    """
    
    # 如果提供了权重列表（list_of_weights）
    if list_of_weights is not None:
        # 检查权重列表和数字列表长度是否一致
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        # 如果没有权重，则默认所有元素权重为 1
        effective_weights = [1] * len(list_of_numbers)

    # 计算每个元素的加权平方
    # 例如 numbers=[2,4], weights=[1,0.5]
    # squares = [1*4, 0.5*16] = [4,8] 
    # 实际上，(1*4 + 0.5*16) / (1 + 0.5) = (4 + 8) / 1.5 = 12 / 1.5 = 8.0 在数学上是正确的
    # python -m doctest squares.py

    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]

    # 返回平方的加权平均值 = 加权平方和 / 权重总和
    return sum(squares) / sum(effective_weights)


def convert_numbers(list_of_strings):
    """将字符串列表转换为数字列表，忽略多余空格。
    
    示例：
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4.0, 8.0, 15.0, 16.0, 23.0, 42.0]
    """
    all_numbers = []  # 用于存储提取出来的数字字符串
    for s in list_of_strings:
        # 把每个字符串拆分成小块（按空格分隔），再去除多余空格
        # 例如 " 23    42 " -> ["23", "42"]
        all_numbers.extend([token.strip() for token in s.split()])

    # 把字符串转成浮点数
    return [float(number_string) for number_string in all_numbers]

def read_file_as_numbers(filename):
    """Read a file and extract all numbers inside."""
    with open(filename, "r") as f:
        lines = f.readlines()
    return convert_numbers(lines)

if __name__ == "__main__":
    # ---------------- argparse 设置 ----------------
    parser = argparse.ArgumentParser(
        description="Compute weighted average of squares from files."
    )

    # numbers 文件
    parser.add_argument(
        "file_numbers",
        help="Text file containing input numbers."
    )

    # 可选 weights 文件
    parser.add_argument(
        "--weights",
        help="Text file containing weights (optional).",
        default=None
    )

    args = parser.parse_args()

    # 读取数字文件
    numbers = read_file_as_numbers(args.file_numbers)

    # 如果提供了 weights 文件，则读取
    if args.weights is not None:
        weights = read_file_as_numbers(args.weights)
    else:
        weights = None

    # 计算结果
    result = average_of_squares(numbers, weights)

    print(result)