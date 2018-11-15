import helper
import simulator

def encrypt(message , key):
    simulator.simulate_inputs(message , key)
    simulator.simulate_init_binary(helper.getBinary(message) , helper.getBinary(key))

    M = helper.applyTable(helper.getBinary(message) , 'ip')
    L0 , R0 = helper.makeHalf(M)

    simulator.simulate_init_iptable_effects(M , L0 , R0)

    K = helper.applyTable(helper.getBinary(key) , "pc1")
    C0 , D0 = helper.makeHalf(K)

    simulator.simulate_init_pc1table_effects(K , C0 , D0)

    Ln = L0
    Rn = R0
    Cn = C0
    Dn = D0
    Kn = K
    for n in range(16):
        simulator.simulate_round_number(n+1)
        Cn = helper.leftShift(Cn , n+1)
        Dn = helper.leftShift(Dn , n+1)
        Kn = helper.applyTable(Cn + Dn , 'pc2')
        tempL = Ln[:]
        Ln = Rn
        ern , xor , sbox , sbox_result =  helper.f(Rn , Kn)

        simulator.simulate_f_calculations(ern , xor , sbox , sbox_result)

        Rn = bin(int(tempL , 2) ^  int(sbox_result , 2))[2:].zfill(32)

        simulator.simulate_round_results(n+1 , Cn , Dn , Kn , Ln , Rn)

    ip1_effect = helper.applyTable(Rn + Ln , 'ip-1')
    final_result = helper.getHexa(ip1_effect)

    simulator.simulate_final_result(ip1_effect , final_result)

    return final_result
