def loan(A, r, n):
    X = (A * ((1 + r) ** n) * r) / ((1 + r) ** n - 1)
    r = r * 100
    print(f'Vay: {A:,.2f} Đồng')
    print(f'Lãi suất: {r:,.2f}%/tháng')
    print(f'Trong: {n: ,.2f} tháng')
    print(f'Mỗi tháng cần trả: {X: ,.3f} Đồng')


loan(3786784723, 0.12, 6)