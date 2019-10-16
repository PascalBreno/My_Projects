# hi, first you need to know your project's location

#The name 'nameMethod' it is name to your 'persistenciaLista'
nameMethod = input('insira o nome da entidade ou 0 para finalizar\n')


while(nameMethod!='0'):

#Here you need change to where your project is (or your folde with 'persistenciaLista')

    arq = open("/home/pascal/Desktop/MagicStore/MagicStore/src/PersistenciaLista/Novo"+nameMethod+"PersistenciaLista.java", "w")
    arq.write('''
package PersistenciaLista;
import Entidades.'''+nameMethod+''';
import Persistencia.persistencia'''+nameMethod+''';
import java.util.ArrayList;
import java.util.List;


public class Novo'''+nameMethod+'''PersistenciaLista 
        implements persistencia'''+nameMethod+''' {

    private List lista = new ArrayList();

    @Override
    public void inserir('''+nameMethod+''' novo'''+nameMethod+''') {
    int ultimoId = 0;
        if (lista.size() > 0) {
            int posicaoUltimo = lista.size() - 1;
            '''+nameMethod+''' ultimo = ('''+nameMethod+''') lista.get(posicaoUltimo);
            ultimoId = ultimo.getId();
        }   
        novo'''+nameMethod+'''.setId(ultimoId + 1);
        lista.add(novo'''+nameMethod+''');
    }

    @Override
    public void alterar('''+nameMethod+''' novo'''+nameMethod+''') {
        for (int i = 0; i < lista.size(); i++) {
            '''+nameMethod+''' elem = ('''+nameMethod+''') lista.get(i);
            if(novo'''+nameMethod+'''.getId() == elem.getId()){
                lista.set(i, novo'''+nameMethod+''');
            }
        }
    }

    @Override
    public void remover('''+nameMethod+''' novo'''+nameMethod+''') {
          int posicao = 0;

        while (posicao < lista.size()) {
            '''+nameMethod+''' elemento = ('''+nameMethod+''') lista.get(posicao);
            if (elemento.getId() == novo'''+nameMethod+'''.getId()) {
                lista.remove(posicao);
                break;
            }
            posicao++;
        }
    }
'''
# ===================Here you need modify to your search...========================= 
'''
    @Override
    public '''+nameMethod+''' buscar(int id) {
         for (int i = 0; i < lista.size(); i++) {
            '''+nameMethod+''' elem = ('''+nameMethod+''') lista.get(i);
            if(elem.getId() == id){
                return elem;
            }
         }
        return null;
    }

    @Override
  public List<'''+nameMethod+'''> getAll(){
      return lista;
  }
 
}''')
    nameMethod = input('insira o nome da entidade ou 0 para finalizar\n')
    arq.close()
