def simulate_inputs(message , key):
    file = open("output.txt" , "a+")
    file.write("Message : {}\nKey: {}\n--------------\n".format(message ,key))
    file.close()

def simulate_init_binary(message , key):
    file = open("output.txt" , "a+")
    file.write("Converting to binary:\n-------------------\n")
    file.write("M : {}\nK : {}\n-------------------------\n".format(message,key))
    file.close()

def simulate_init_iptable_effects(M , L0 , R0):
    file = open("output.txt" , "a+")
    file.write("After applying Ip table on M:\n--------------------------\n")
    file.write("M : {}\nLo : {}\nRo : {}\n------------------\n".format(M , L0 , R0))
    file.close()

def simulate_init_pc1table_effects(K , C0 , D0):
    file = open("output.txt" , "a+")
    file.write("After applying Pc-1 table on K:\n--------------------------\n")
    file.write("K : {}\nCo : {}\nDo : {}\n------------------\n".format(K , C0 , D0))
    file.close()
def simulate_round_number(round):
    file = open("output.txt" , "a+")
    file.write("Round {}\n-----------------------------\n".format(round))
    file.close()
def simulate_f_calculations(ern , xor , sbox , sbox_result):
    file = open("output.txt" , "a+")
    file.write("ER: {}\n".format(ern))
    file.write("K + ER: {}\n".format(xor))
    file.write("SBOX: {}\n".format(sbox))
    file.write("After P table: {}\n".format(sbox_result))
    file.close()
def simulate_round_results(round , Cn , Dn , Kn , Ln , Rn):
    file = open("output.txt" , "a+")
    file.write("C{} : {}\nD{} : {}\nK{} : {}\nL{} : {}\nR{} : {}\n".format(
        round , Cn , round , Dn , round , Kn , round , Ln , round , Rn
    ))
    file.close()

def simulate_final_result(ip1_effect , final_result):
    file = open("output.txt" , "a+")
    file.write("After applying Ip-1 table on R16L16:\n--------------------------\n")
    file.write("Ip-1 : {}\n------------------\n".format(ip1_effect))
    file.write("The hexa format: {}\n------------------\n".format(final_result))
    file.close()
