# hi, first you need know to where is your project 

#The name '+nameMethod+' it is name to your 'persistenciaLista'
nameMethod = input('insira o nome da entidade ou 0 para finalizar\n')


while(nameMethod!='0'):

#Here you need change to where your project is (or your folde with 'persistenciaLista')

    arq = open("/home/pascal/Desktop/MagicStore/MagicStore/src/PersistenciaArquivo/"+nameMethod+"PersistenciaArquivo.java", "w")
    arq.write('''import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.List;

public class '''+nameMethod+'''PersistenciaArquivo
        extends '''+nameMethod+'''PersistenciaLista
        implements persistencia'''+nameMethod+''' {

    private final String arq = "'''+nameMethod+'''.db";
    public '''+nameMethod+'''PersistenciaArquivo(){
        ler();
    }
    private void ler() {
        try {
            ObjectInputStream ois;
            FileInputStream fis;
            fis = new FileInputStream(arq);
            ois = new ObjectInputStream(fis);
            lista = (List) ois.readObject();
            ois.close();
        } catch (Exception erro) {
            erro.printStackTrace();
        }
    }
    private void gravar(){
        try{
            ObjectOutputStream oos;
            FileOutputStream fos;
            fos = new FileOutputStream(arq);
            oos = new ObjectOutputStream(fos);
            oos.writeObject(lista);
            oos.close();
        }catch(Exception erro){
            erro.printStackTrace();
        }
    }
    public void inserir('''+nameMethod+''' novo'''+nameMethod+''') {
        super.inserir(novo'''+nameMethod+''');
        gravar();
    }
    public void alterar('''+nameMethod+''' novo'''+nameMethod+''') {
        super.alterar(novo'''+nameMethod+''');
        gravar();
    }
    public void remover('''+nameMethod+''' novo'''+nameMethod+''') {
        super.remover(novo'''+nameMethod+''');
        gravar();
    }
}

''')
    nameMethod = input('insira o nome da entidade ou 0 para finalizar\n')
    arq.close()
