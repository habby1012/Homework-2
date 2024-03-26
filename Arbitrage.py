liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}


def exchange(amount, pair):
    if pair in liquidity:
        reserve_src, reserve_dest = liquidity[pair]
    else:
        pair = (pair[1], pair[0])
        reserve_dest, reserve_src = liquidity[pair]

    amount_out = (amount * reserve_dest) / (reserve_src + amount)
    return amount_out

def find_profitable_path(start_token, current_token, amount, path, visited):
    if current_token == start_token and path != []:
        if amount > 20:
            return (True, path, amount)
        return (False, path, amount)
    
    for token in ['tokenA', 'tokenB', 'tokenC', 'tokenD', 'tokenE']:
        if token not in visited or (token == start_token and len(path) > 1):
            pair = (current_token, token)
            if pair in liquidity or (token, current_token) in liquidity:
                amount_out = exchange(amount, pair)
                found, found_path, found_amount = find_profitable_path(start_token, token, amount_out, path + [token], visited | {token})
                if found:
                    return (True, found_path, found_amount)
    return (False, path, amount)

found, path, amount = find_profitable_path('tokenB', 'tokenB', 5, [], set())
if found:
    complete_path = ['tokenB'] + path
    print(f"path: {'->'.join(complete_path)}, tokenB balance={amount:.6f}")
else:
    print("No profitable path found.")
