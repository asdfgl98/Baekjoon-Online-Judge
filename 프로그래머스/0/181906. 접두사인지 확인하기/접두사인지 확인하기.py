def solution(my_string, is_prefix):       
    return 0 if len(my_string) < len(is_prefix) else 1 if all(my_string[i] == is_prefix[i] for i in range(len(is_prefix))) else 0