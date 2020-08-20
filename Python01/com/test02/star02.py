# -*- coding:utf-8 -*-

#Join

# 1.
# \n이랑 조인할거야  =>얘랑! [''.join(['*' for i in range(i + 1)]) for i in range(5)])
# i가 0부터 4까지 돌면서 [''.join(['*' for i in range(i + 1)] <= 출력해줄거야.
# for i in range(5)이 한번 반복하면서 ['*' for i in range(i + 1)]를 출력해줘. 1부터 5까지.
# i가 0일때 => ''.join(['*']) => '*'
# i가 1일때 => ''.join(['*', '*']) => "**"
# ...반복
print('\n'.join([''.join(['*' for i in range(i + 1)]) for i in range(5)]))
print('——')

# 2
print('\n'.join([''.join(['*' for i in range(i)]) for i in range(5, 0, -1)]))
print('——')

# 3
print('\n'.join([''.join([' ' for i in range(4 - i)] + ['*' for i in range(i + 1)]) for i in range(5)]))
print('——')

# 4
print('\n'.join([''.join([' ' for i in range(i)] + ['*' for i in range(5 - i)]) for i in range(5)]))
print('——')

# 5
print('\n'.join([''.join([' ' for i in range(4 - i)] + ['*' for i in range(2 * i + 1)]) for i in range(5)]))
print('——')