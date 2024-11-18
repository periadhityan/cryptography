import generate_RSA, wiener_attack, simple_RSA, sage_gen_rsa

def main():
    
    #e, n, d = generate_RSA.gen_vulnerable_keys()
    #e, n, d = simple_RSA.RSA()

    #vuln = True
    vuln = False

    if(vuln):
        #Vulnerable set
        print("Using Vulnerable RSA Keys")
        e = 30749686305802061816334591167284030734478031427751495527922388099381921172620569310945418007467306454160014597828390709770861577479329793948103408489494025272834473555854835044153374978554414416305012267643957838998648651100705446875979573675767605387333733876537528353237076626094553367977134079292593746416875606876735717905892280664538346000950343671655257046364067221469807138232820446015769882472160551840052921930357988334306659120253114790638496480092361951536576427295789429197483597859657977832368912534761100269065509351345050758943674651053419982561094432258103614830448382949765459939698951824447818497599
        n = 109966163992903243770643456296093759130737510333736483352345488643432614201030629970207047930115652268531222079508230987041869779760776072105738457123387124961036111210544028669181361694095594938869077306417325203381820822917059651429857093388618818437282624857927551285811542685269229705594166370426152128895901914709902037365652575730201897361139518816164746228733410283595236405985958414491372301878718635708605256444921222945267625853091126691358833453283744166617463257821375566155675868452032401961727814314481343467702299949407935602389342183536222842556906657001984320973035314726867840698884052182976760066141
    else:
        #Non Vulnerable Set
        print("Generating Non Vulnerable RSA Keys")
        n, e, d = sage_gen_rsa.sage_rsa()


    print("Bit Length of Encryption Exponent E = ", e.bit_length())
    print("Bit Length of Public Modulus N = ", n.bit_length())

    message = input("Enter mesage to encrypt: ")
    print()

    #print("Public Encryption Component E =", e)
    #print("Public Modulus N = ", n)
    #print("Private Decryption Exponent D = ", d)

    #print("Plain Text Message = ", message)
    encoded_message = [ord(c) for c in message]
    #print("Encoded message = ", encoded_message)

    ciphertext = [pow(c, e, n) for c in encoded_message]
    #print("Cipher Text = ", ciphertext)

    print("Using Wiener's Attack to Decrypt Cipher Text")
    print()

    wiener_d = wiener_attack.wiener_attack(e, n)

    if(wiener_d == "Decryption Exponent Not Found"):
        print(wiener_d)
        print("This Decryption Exponent is NOT Vulnerable to Wiener's Attack")
        return
    
    print()
    print("Decryption Exponent D Found Using Wiener's Attack = ", wiener_d)
    print("Bit Length of Decryption Exponent D = ", wiener_d.bit_length())
    print()
    valid_param = (wiener_d**4)*3

    if(valid_param < n):
        print("This Decryption Exponent is Vulnerable to Wiener's Attack")
        print()

    print("Decrypting Cipher Text")

    encoded_plaintext = [pow(c, wiener_d, n) for c in ciphertext]
    plaintext = "".join(chr(c) for c in encoded_plaintext)

    print("Decrypted Message = ", plaintext)


main()