import json

def clean_timed_out_tasks(file_path):
    # 读取JSON文件
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 过滤掉包含超时响应的task
    cleaned_data = []
    for task in data:
        has_timeout = False
        for response in task['query_response']:
            if response['response'] == "Function call timed out":
                has_timeout = True
                break
        
        if not has_timeout:
            cleaned_data.append(task)
    
    # 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, indent=4, ensure_ascii=False)
    
    # 打印统计信息
    print(f"原始task数量: {len(data)}")
    print(f"清理后task数量: {len(cleaned_data)}")
    print(f"删除的task数量: {len(data) - len(cleaned_data)}")

# 使用示例
file_path = "MEGA-Bench/megabench/result/Phi4/all_query_responses.json"
clean_timed_out_tasks(file_path)