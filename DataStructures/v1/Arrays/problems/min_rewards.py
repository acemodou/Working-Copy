import pytest 


# def minRewards(scores):
#     rewards = [1] * len(scores)
#     for i in range(1, len(scores)):
#         j = i - 1
#         if scores[i] > scores[j]:
#             rewards[i] = rewards[j]+1
#         else:
#             while j >=0 and scores[j] > scores[j+1]:
#                 rewards[j] = max(rewards[j], rewards[j+1]+1)
#                 j -= 1
#     return sum(rewards)

# def minRewards(scores):
#     rewards = [1] * len(scores)
#     local_minimum = get_local_minimum(scores)
#     for local_idx in local_minimum:
#         expand_outward(local_idx, scores, rewards)
#     return sum(rewards)

# def get_local_minimum(array):
#     if len(array) == 1:
#         return array[0]
    
#     store_local_mins = []
#     for i in range(len(array)):
#         if i == 0 and array[i] < array[i+1]:
#             store_local_mins.append(i)
#         if i == len(array)-1 and array[i] < array[i-1]:
#             store_local_mins.append(i)
#         if i == 0 or i == len(array)-1:
#             continue 
#         if array[i-1] > array[i] < array[i+1]:
#             store_local_mins.append(i)
#     return store_local_mins

# def expand_outward(local_idx, scores, rewards):
#     expand_left_from_local_idx = local_idx - 1
#     while expand_left_from_local_idx >=0 and scores[expand_left_from_local_idx] > scores[expand_left_from_local_idx+1]:
#         rewards[expand_left_from_local_idx] = max(rewards[expand_left_from_local_idx], rewards[expand_left_from_local_idx+1]+1)
#         expand_left_from_local_idx -= 1
#     expand_right_from_local_idx = local_idx + 1
#     while expand_right_from_local_idx < len(scores) and scores[expand_right_from_local_idx] > scores[expand_right_from_local_idx-1]:
#         rewards[expand_right_from_local_idx] = rewards[expand_right_from_local_idx-1] + 1
#         expand_right_from_local_idx += 1
#     return rewards

def minRewards(scores):
    rewards = [1] * len(scores)

    for idx in range(1, len(scores)):
        if scores[idx] > scores[idx -1]:
            rewards[idx] = rewards[idx-1] + 1
    for idx in reversed(range(len(scores)-1)):
        if scores[idx] > scores[idx+1]:
            rewards[idx] = max(rewards[idx], rewards[idx+1]+1)
    return sum(rewards)


@pytest.mark.parametrize(
    'input, expected',
    [
        ([4, 2, 1, 3], 8),
        ([8, 4, 2, 1, 3, 6, 7, 9, 5], 25),
        ( [5, 10], 3)
    ]
)

def test_min_rewards(input, expected):
    assert minRewards(input) == expected 


if __name__=="__main__":
    pytest.main([__file__])
