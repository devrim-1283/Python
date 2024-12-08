def permute(elements, current):
    if len(elements) == 0: 
        return [current] 
    else:
        result = []
        for i in range(len(elements)):
            remaining = elements[:i] + elements[i+1:]
            new_current = current + elements[i]
            result.extend(permute(remaining, new_current))
        return result