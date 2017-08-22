# hi, first you need know to where is your project 

#The name 'nameMethod' it is name to your 'persistencia'
nameMethod = input('insira o nome da entidade ou 0 para finalizar\n')


while(nameMethod!='0'):
#Here you need change to where your project is (or your folde with 'persistencia')

    arq = open("/home/pascal/Desktop/MagicStore/MagicStore/src/Persistencia/persistencia"+nameMethod+".java", "w")
    arq.write('''
package Persistencia;

import Entidades.'''+nameMethod+''';
import java.util.List;

'''
#Obs. I use in my 'persistencia' Name novoName. If your project have 'Name nome' change nome+nameMethod to 'nameMethod.lower()' to make your String with Small letters
'''
public interface persistencia'''+nameMethod+''' {
    public void inserir('''+nameMethod+''' novo'''+nameMethod+''');
    
    public void alterar('''+nameMethod+''' novo'''+nameMethod+''');
    
    public void remover('''+nameMethod+''' novo'''+nameMethod+''');
    
    public List<'''+nameMethod+'''> getAll();
}''')
    nameMethod = input('insira o nome da entidade ou 0 para finalizar\n')
    arq.close()
