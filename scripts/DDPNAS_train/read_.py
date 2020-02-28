import glob
import os

folder_list = glob.glob("/userhome/project/Auto_NAS_V2/experiments/DDPNAS_V2/darts/cifar10/*")
# print(folder_list)
this_dict  = {}
this_dict_3_4 = {}
folder_list.sort()
for i in folder_list:
    for j in range(9):
        this_str = 'pruning_step_' + str(j + 1)
        if this_str in i:
            file = open(os.path.join(i, 'logger.log'))
            lines = file.readlines()
            genotype = lines[-4][36:-1]
            file.close()
            file = open(os.path.join(i, 'network_info', '3_4_False.txt'))
            lines = file.readlines()
            genotype_3_4 = lines[0][:-1]
            file.close()
            flag = 0
            key_this_str = this_str + '_' + str(flag)
            while key_this_str in this_dict.keys():
                flag += 1
                key_this_str = this_str + '_' + str(flag)
            this_dict[key_this_str] = genotype

            flag = 0
            key_this_str = this_str + '_3_4_' + str(flag)
            while key_this_str in this_dict_3_4.keys():
                flag += 1
                key_this_str = this_str + '_3_4_' + str(flag)
            this_dict_3_4[key_this_str] = genotype_3_4
print(this_dict)
print('\n')
print(this_dict_3_4)

