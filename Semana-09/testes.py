import unittest;
import aluno as a;
import turma as t;

class turmaTest(unittest.TestCase):

  def setUp(self):
    print('Teste', self._testMethodName, 'sendo executado...');
    self.alunos = [];

    self.alunos.append(a.Aluno('Fabio', 'Teixeira', 10));
    self.alunos.append(a.Aluno('Angela', 'Teixeira', 7));     
    self.alunos.append(a.Aluno('Fabiano', 'Teixeira', 8));     
    self.alunos.append(a.Aluno('Melissa', 'Teixeira', 6));  
    
    self.turmaObject = t.Turma();
    self.turmaObject.cadastrarAlunos(self.alunos);
  
  def tearDown(self):
    print('Teste', self._testMethodName, 'finalizado.'); 
  
  def testMaior(self):      
    self.assertEqual(10, self.turmaObject.maiorNota.nota, 'Erro ao encontrar maior nota');

  def testMenor(self):    
    self.assertEqual(6, self.turmaObject.menorNota.nota, 'Erro ao encontrar menor nota');

  def testIntervalo(self):
    print('Testar se o intervalo de notas está correto.')
    #Escreva o seu código aqui
    #Testar se o intervalo de notas está entre 0 e 10.
    for aluno in self.turmaObject.turma:
      self.assertGreaterEqual(aluno.nota, 0, 'Erro: Nota menor que 0');
      self.assertLessEqual(aluno.nota, 10, 'Erro: Nota maior que 10');


if __name__ == "__main__":
  unittest.main()