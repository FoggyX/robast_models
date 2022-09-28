def main():
    open_close = {'(': ')', '{': '}', '[': ']'}
    close_open = {')': '(', '}': '{', ']': '['}

    string = input()
    stack = []

    result = True

    for symbol in string:
        if symbol in open_close:
            stack.append(symbol)
        elif symbol in close_open:
            if len(stack):
                bracket = stack.pop()
                if bracket != close_open[symbol]:
                    result = False
                    break
            else:
                result = False
                break
    if len(stack):
        result = False

    print(result)

if __name__ == '__main__':
    main()
