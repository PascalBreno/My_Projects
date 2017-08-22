
package Persistencia;

import Entidades.breno;
import java.util.List;

/**
 *
 * @author pascal
 */
public interface persistenciabreno {
    public void inserir(breno novobreno);
    
    public void alterar(breno novobreno);
    
    public void remover(breno novobreno);
    
    public List<breno> getAll();
}