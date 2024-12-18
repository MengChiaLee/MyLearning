import numpy as np

# 設定精度範圍
precisions = [10**(-i) for i in range(1, 8)]
max_attempts = 100
max_points = 10000

# 結果儲存
results = []

for precision in precisions:
    success_count = 0
    pi_values = []
    
    for _ in range(max_attempts):
        inside_circle = 0
        total_points = 0
        
        # 隨機點生成
        while total_points < max_points:
            x, y = np.random.uniform(0, 1, 2)
            if x**2 + y**2 <= 1:
                inside_circle += 1
            total_points += 1
            
            # 計算 \(\pi\) 值
            approx_pi = 4 * inside_circle / total_points
            if abs(approx_pi - np.pi) < precision:
                success_count += 1
                pi_values.append(approx_pi)
                break

        # 若未成功達到目標精度
        if total_points >= max_points:
            pi_values.append(None)

    # 計算成功的平均值
    successful_values = [val for val in pi_values if val is not None]
    avg_pi = np.mean(successful_values) if successful_values else None
    results.append((precision, success_count, avg_pi))

# 輸出結果
for precision, success_count, avg_pi in results:
    if avg_pi is not None:
        print(f"{precision:.1e} success {success_count} times {avg_pi}")
    else:
        print(f"{precision:.1e} no success")
