# Лебедев Евгений: Получение и вывод данных о валидаторах сети NEAR

import os

command_line_command = 'near validators current'

print('Blockchain: NEAR Protocol (NEAR)')
print('Election mechanism: Thresholded Proof-of-Stake (TPoS)')
os.system(command_line_command)