from typing import Any, Callable, Dict, List

from factorial_typed import factorial


def map_int_list(fnc: Callable, list_received: List[int]) -> List[int]:
    return [fnc(e) for e in list_received]


# def map_int_dict(fnc: Callable, dict_received: Dict[Any, int]) -> Dict[Any, int]:
#    return {key: fnc(value) for key, value in dict_received.items()}


print(map_int_list(factorial, [0, 1, 2, 3, 40.1]))
# print(map_int_dict(factorial, {'zero': 1, 'one': 1, 'three': 3}))
