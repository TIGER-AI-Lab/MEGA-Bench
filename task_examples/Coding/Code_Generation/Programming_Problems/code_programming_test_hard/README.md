# Task: code_programming_test_hard

## Task Description:

```
Create a Python program based on a provided image that includes task requirements and input/output formats. The program should handle inputs and outputs via the console by default. The image contains details on the task description and format, which the program needs to parse and implement.
```

## The 1-shot Example for Task Demonstration:

```
Demonstration example(s) of the task:
Example 1:
```

![Image](1.png)

```
Example Question: Given image(s) that includes program requirements and console input/output formats, write a Python program that meets these requirements.
Example Response:
[PLEASE OUTPUT YOUR REASONING]
Answer: def inorder(arr, tree, root, idx, n):
    if root >= n:
        return
    inorder(arr, tree, 2 * root + 1, idx, n)
    tree[root] = arr[idx[0]] 
    idx[0] += 1
    inorder(arr, tree, 2 * root + 2, idx, n)  

def level_order(tree, n):
    print(" ".join(map(str, tree[:n])))

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    tree = [None] * n
    idx = [0]
    
    inorder(arr, tree, 0, idx, n)
    level_order(tree, n) 

if __name__ == "__main__":
    main()
Answer the new question below. The last part of your response should be of the following format: "Answer: <YOUR ANSWER>" (without angle brackets) where YOUR ANSWER is your answer, following the same task logic and output format of the demonstration example(s). For your answer, do not output additional contents that violate the specified format. Think step by step before answering.
```

## Additional Task Information:

- **ID**: 590
- **Eval Context**: {'test_case': {'input': ['00100 6 4', '00000 4 99999', '00100 1 12309', '68237 6 -1', '33218 3 00000', '99999 5 68237', '12309 2 33218'], 'expected': '00000 4 33218\n33218 3 12309\n12309 2 00100\n00100 1 99999\n99999 5 68237\n68237 6 -1'}}
- **Taxonomy Tree Path**: Coding;Code_Generation;Programming_Problems
- **App**: Coding
- **Input Format**: Text-Based Images and Documents
- **Output Format**: structured_output
- **Metric Info**:
  - **Field Score Function**: {'Output': 'program_judge'}
  - **Aggregation**: {'function': 'mean', 'field_weights': {'Output': 1}}
  - **Response Parse Function**: answer_string
