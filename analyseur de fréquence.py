import matplotlib.pyplot as plt
from collections import Counter
import tkinter as tk  # graphique 


alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z','A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z'
]

lettres_fr = [
    'E', 'A', 'S', 'I', 'N', 'T', 'R', 'L', 'U', 'O',
    'D', 'C', 'M', 'P', 'G', 'V', 'B', 'F', 'Q', 'H',
    'X', 'J', 'Y', 'K', 'W', 'Z'
]

frequences_fr = [
    17.3, 8.4, 8.1, 7.3, 7.1, 7.1, 6.6, 6.0, 5.7, 5.3,
    4.2, 3.0, 3.0, 3.0, 1.3, 1.3, 1.1, 1.1, 1.0, 0.9,
    0.4, 0.3, 0.3, 0.1, 0.1, 0.1
]

# Fréquences des lettres en anglais
lettres_en = [
    'E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'L',
    'D', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B',
    'V', 'K', 'J', 'X', 'Q', 'Z'
]

frequences_en = [
    12.7, 9.1, 8.2, 7.5, 7.0, 6.7, 6.3, 6.1, 6.0, 4.0,
    4.3, 2.8, 2.8, 2.4, 2.4, 2.2, 2.0, 2.0, 1.9, 1.5,
    1.0, 0.8, 0.2, 0.2, 0.1, 0.1
]

# Fréquences des lettres en espagnol
lettres_es = ['E', 'A', 'O', 'S', 'R', 'N', 'I', 'D', 'L', 'C', 'T', 'U', 'M', 'P', 'B', 'G', 'V', 'Y', 'Q', 'H', 'F', 'Z', 'J', 'Ñ', 'X']
frequences_es = [13.7, 11.7, 8.7, 7.9, 6.9, 6.7, 6.2, 5.0, 4.9, 4.6, 4.6, 3.9, 3.1, 2.5, 1.4, 1.0, 0.9, 0.9, 0.9, 0.7, 0.7, 0.5, 0.4, 0.3, 0.1]

# --- Fonction d'analyse fréquentielle ---
def frequency_analysis(text):
    L = [" ", ".", ",", "'"]
    for i in L:
        text = text.replace(i, "").upper()
        text = text.replace('\t' , '')
        text = text.replace('\n', '')
        text = text.replace('À', 'A')
        text = text.replace('Â', 'A')
        text = text.replace('É', 'E')
        text = text.replace('È', 'E')
        text = text.replace('Ç', 'C')

    

    print(text)
    frequency = Counter(text)  # retourner un objet counter (se comporte comme un dictionnaire regroupant caractère et son nbr d'occurence counter({'E' : 85 , 'S':50 , .....} ) )
    print(frequency)
    sorted_frequency = dict(frequency.most_common())  # frequency.most_common() retourne une liste de tuple d'un objet counter ==>list : [('E',85),('S',50) , .....]
                                                      # dict([('E',85),('S',50) , .....]) ==>dict :  {'E' : 85 , 'S':50 , .....} 
    
    La=list()
    Lb=list()
    for key,val in sorted_frequency.items() : 
        La.append(key)
        Lb.append(val)
    let =La[Lb.index(max(Lb))]    # extraire le caractère qui a le plus grand nombre d'occurence 
    return sorted_frequency , let 



def calculate_decal(let , lang):
    if lang=='fr':
        return alphabet.index('E')- alphabet.index(let)





def decrypter(text ,decal) :
    list_decal = list()
    dec_r = 0 
    for i in range(26) : 
    
        if i - decal <0 : 
            dec_r = i -decal +26
        else:
            dec_r = i-decal 

        list_decal.append(alphabet[dec_r])

    dict_mapping= dict(zip(alphabet , list_decal))
    plain_text = ''.join([dict_mapping.get(c, c) for c in text])
    return plain_text

     

#Fonction déclenchée lors de l'apuis sur valider 
def submit_text():
    global cipher_text
    cipher_text = text_zone.get("1.0", tk.END).upper()         # Récupérer texte depuis la zone graphique

    freq_analysis,let = frequency_analysis(cipher_text)

    decal= calculate_decal(let ,'fr')
    print(decal)
    plain_text =decrypter(cipher_text, decal)

    affichage = tk.Text(root, height=10, width=50)  # Ajuste la taille selon ton besoin
    affichage.insert(tk.END, plain_text)  # Insère le texte déchiffré dans la zone
    affichage.config(state=tk.DISABLED)  # Rendre la zone en lecture seule
    affichage.pack(pady=7, padx=7)

    letters = list(freq_analysis.keys())
    frequencies = list(freq_analysis.values())

    
    plt.figure(figsize=(10, 6))
    plt.bar(letters, frequencies, color='skyblue')
    plt.xlabel('Lettres')
    plt.ylabel('Fréquence')
    plt.title('Analyse de la fréquence des lettres dans le texte')
    plt.show()

    root.destroy()# ferme la fenêtre après avoir récupéré le texte 






# ************** Interface graphique ************
root = tk.Tk()
root.title("Analyseur fréquentielle")

label = tk.Label(root, text="Mettre ton texte ici ")
label.pack(pady=2)

text_zone = tk.Text(root, height=10, width=50)
text_zone.pack(pady=7, padx=7)

button = tk.Button(root, text="Analyser", command=submit_text)
button.pack(pady=5)

root.mainloop()

# letters = list(freq_analysis.keys())
# frequencies = list(freq_analysis.values())
# plt.figure(figsize=(10, 6))
# plt.bar(letters, frequencies, color='skyblue')
# plt.xlabel('Lettres')
# plt.ylabel('Fréquence')
# plt.title('Analyse de la fréquence des lettres dans le texte')
# plt.show()



def rotate(text,let) :                    # let  : c'est le caractèere avec plus grand nbre d'occurence 
   
        decal = alphabet.index('E') - alphabet.index(let)            # déterminer le décalage 
         
        if decal>0 : 
            decal_list = list()
            for i in range(26) :
                sum = i+decal
                if sum <=25 : 
                    decal_list.append((alphabet[i] ,alphabet[sum] ))
                else :
                    decal_list.append((alphabet[i] ,alphabet[i-26] ))
                
                
            text.replace()


    



