import src.EulerHelpers as Euler
import math
import tqdm


def xor_list(number_list, key_seq):
    new_list = []
    for i, number in enumerate(number_list):
        cycle_len = len(key_seq)
        new_list.append(number ^ key_seq[i % cycle_len])

    return new_list


def decrypt_message(message_path):
    with open(message_path, mode='r') as file:
        txt = file.read().strip()
    num_list = [int(x) for x in txt.split(',')]

    for i in tqdm.tqdm(range(97, 122 + 1)):
        for j in range(97, 122 + 1):
            for k in range(97, 122 + 1):
                key = (i, j, k)
                decrypted = ''.join(chr(x) for x in xor_list(num_list, key))
                if ' the ' in decrypted:
                    print(decrypted)
                    return decrypted, key


if __name__ == '__main__':
    my_path = Euler.get_path(r'src/misc/p059_cipher.txt')
    message, key = decrypt_message(my_path)
    print("sum of decrypted ascii characters = ", sum(ord(x) for x in message))
