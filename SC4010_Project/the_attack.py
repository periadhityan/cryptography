import wiener_attack, generate_rsa
from sage.all import *

def main():

    inp_val = False

    while not inp_val:
        print("1. Generate Vulnerable RSA keys")
        print("2. Generate Strong RSA keys")
        print("3. SMU Paper Values (Strong)")
        print("4. SMU Paper Values (Vulnerable)")
        choice = input("Enter your choice: ")

        if(choice == '1' or choice == '2' or choice == '3' or choice == '4'):
            inp_val = True
        else:
            print("Invalid Choice")
        

    if(choice == "1"):
        #Vulnerable set
        print("Generating Vulnerable RSA Keys\n")
        n, e, d = generate_rsa.vulnerable_rsa()

        #e = 30749686305802061816334591167284030734478031427751495527922388099381921172620569310945418007467306454160014597828390709770861577479329793948103408489494025272834473555854835044153374978554414416305012267643957838998648651100705446875979573675767605387333733876537528353237076626094553367977134079292593746416875606876735717905892280664538346000950343671655257046364067221469807138232820446015769882472160551840052921930357988334306659120253114790638496480092361951536576427295789429197483597859657977832368912534761100269065509351345050758943674651053419982561094432258103614830448382949765459939698951824447818497599
        #n = 109966163992903243770643456296093759130737510333736483352345488643432614201030629970207047930115652268531222079508230987041869779760776072105738457123387124961036111210544028669181361694095594938869077306417325203381820822917059651429857093388618818437282624857927551285811542685269229705594166370426152128895901914709902037365652575730201897361139518816164746228733410283595236405985958414491372301878718635708605256444921222945267625853091126691358833453283744166617463257821375566155675868452032401961727814314481343467702299949407935602389342183536222842556906657001984320973035314726867840698884052182976760066141


    if(choice == "2"):
        #Non Vulnerable Set
        print("Generating Non Vulnerable RSA Keys\n")
        n, e, d = generate_rsa.strong_rsa()

    if(choice == '3'):
        n, e, d = generate_rsa.smu_paper_strong()
    
    if(choice == '4'):
        n, e, d = generate_rsa.smu_paper_vulnerable()

    print("Bit Length of Encryption Exponent E = {}\n".format(e.bit_length()))
    print("Bit Length of Public Modulus N = {}\n".format(n.bit_length()))

    message = input("Enter mesage to encrypt: ")
    print("\n")

    encoded_message = [ord(c) for c in message]

    ciphertext = [pow(c, e, n) for c in encoded_message]

    print("Using Wiener's Attack to Decrypt Cipher Text\n")

    wiener_d = wiener_attack.wiener_attack(e, n)
    wiener_param = real_nth_root(n, 4)
    bound_1 = real_nth_root(n, 4)/2
    new_bound = real_nth_root(n, 4)*(1/real_nth_root(18, 4))
    boneh_param = real_nth_root(n, 4)/3

    if(wiener_d == "Decryption Exponent Not Found"):
        print(wiener_d)
        print("This Decryption Exponent is NOT Vulnerable to Wiener's Attack")
        print("Bit Length of Decryption Exponent D = {}\n".format(d.bit_length()))
        if(d>boneh_param):
            print("Decryption Exponent larger than basis of Wiener Attack for Boneh's Bound\n")

        if(d < wiener_param and d > bound_1):
            print("However, this Decryption Exponent fits the basis for Wiener's Attack for Wiener's original Bound")
            print("Wiener's attack works for all d < N^1/4 is disproven\n")
        return
    
    print("Wiener Attack Succesful\n")
    print("Decryption Exponent D Found Using Wiener's Attack = {}\n".format(wiener_d))
    print("Bit Length of Decryption Exponent D = {}\n".format(wiener_d.bit_length()))

    if(d < boneh_param):
        print("This Decryption Exponent is Vulnerable to Wiener's Attack")

    if(d > boneh_param):
        print("This Decryption Exponent is above Boneh's Bound\n")
    
    """if(d == new_bound):
        print("This Decryption Exponent is lower than the new bound\n")"""


    print("Decrypting Cipher Text")

    encoded_plaintext = [pow(c, wiener_d, n) for c in ciphertext]
    plaintext = "".join(chr(c) for c in encoded_plaintext)

    print("Decrypted Message = {}\n".format(plaintext))
    print()

def find_bound():
    found = False
    bound = 1020
    prime_bits = 2048

    while not found:
        n, e, d = generate_rsa.gen_rsa(bound, prime_bits)
        wiener_d = wiener_attack.wiener_attack(e, n)
        if(wiener_d == "Decryption Exponent Not Found"):
            found = True
        else:
            print("Decryption Exponent of {} bits is able to be cracked".format(bound))
            bound = bound + 1
    
    print(bound)
    print("Bit Length of n = ", n.bit_length())
        
        

main()
#find_bound()

