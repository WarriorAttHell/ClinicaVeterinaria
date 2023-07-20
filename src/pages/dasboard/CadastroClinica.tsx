import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const CadastroClinica = () => {
  const navigate = useNavigate();
  const [nome_clinica, setNomeClinica] = useState('');
  const [cnpj, setCnpj] = useState('');
  const [inscricao_estadual, setInscricaoEstadual] = useState('');
  const [inscricao_municipal, setInscricaoMunicipal] = useState('');
  const [endereco, setEndereco] = useState('');
  const [bairro, setBairro] = useState('');
  const [cep, setCep] = useState('');
  const [municipio, setMunicipio] = useState('');
  const [uf, setUf] = useState('');
  const [status, setStatus] = useState('');

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    const formData = {
      nome_clinica,
      cnpj,
      inscricao_estadual,
      inscricao_municipal,
      endereco,
      bairro,
      cep,
      municipio,
      uf,
      status,
    };

    try {
      // Aqui você pode realizar a lógica para enviar os dados do formulário
      // Por exemplo, você pode fazer uma requisição HTTP para enviar os dados para um servidor

      // Exemplo de envio assíncrono usando fetch:
      await fetch('https://veterinaria.offcurve.com.br/api/v1/clinica/add_clinica/', {

        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      // Limpar os campos do formulário após o envio bem-sucedido
      setNomeClinica('');
      setCnpj('');
      setInscricaoEstadual('');
      setInscricaoMunicipal('');
      setEndereco('');
      setBairro('');
      setCep('');
      setMunicipio('');
      setUf('');
      setStatus('');

      // Redirecionar para a lista de clínicas após o cadastro
      navigate('/lista-clinicas');
    } catch (error) {
      // Aqui você pode tratar o erro caso ocorra algum problema durante o envio do formulário
      console.error('Erro ao enviar formulário:', error);
    }
  };

  return (
    <div className="container">
      <h1>Cadastro Clínica</h1>
      <br />
      <form onSubmit={handleSubmit}>
      <div className="form-group">
            <label htmlFor="nomeClinica">Nome da Clínica:</label>
            <input
              type="text"
              className="form-control"
              id="nomeClinica"
              placeholder="Digite o nome da clínica"
              value={nome_clinica}
              onChange={(event) => setNomeClinica(event.target.value)}
            />
          </div>
          <div className="form-group">
            <label htmlFor="cnpj">CNPJ:</label>
            <input
              type="text"
              className="form-control"
              id="cnpj"
              placeholder="Digite o CNPJ"
              value={cnpj}
              onChange={(event) => setCnpj(event.target.value)}
            />
          </div>
          <div className="form-group">
            <label htmlFor="inscricaoEstadual">Inscrição Estadual:</label>
            <input
              type="text"
              className="form-control"
              id="inscricaoEstadual"
              placeholder="Digite a inscrição estadual"
              value={inscricao_estadual}
              onChange={(event) => setInscricaoEstadual(event.target.value)}
            />
          </div>
          <div className="form-group">
            <label htmlFor="inscricaoMunicipal">Inscrição Municipal:</label>
            <input
              type="text"
              className="form-control"
              id="inscricaoMunicipal"
              placeholder="Digite a inscrição municipal"
              value={inscricao_municipal}
              onChange={(event) => setInscricaoMunicipal(event.target.value)}
            />
          </div>
          <div className="form-group">
            <label htmlFor="endereco">Endereço:</label>
            <input
              type="text"
              className="form-control"
              id="endereco"
              placeholder="Digite o endereço"
              value={endereco}
              onChange={(event) => setEndereco(event.target.value)}
            />
          </div>
          <div className="form-group">
            <label htmlFor="bairro">Bairro:</label>
            <input
              type="text"
              className="form-control"
              id="bairro"
              placeholder="Digite o bairro"
              value={bairro}
              onChange={(event) => setBairro(event.target.value)}
            />
          </div>
          <div className="form-group">
            <label htmlFor="cep">CEP:</label>
            <input
              type="text"
              className="form-control"
              id="cep"
              placeholder="Digite o CEP"
              value={cep}
              onChange={(event) => setCep(event.target.value)}
            />
          </div>
          <div className="form-group">
            <label htmlFor="municipio">Município:</label>
            <input
              type="text"
              className="form-control"
              id="municipio"
              placeholder="Digite o município"
              value={municipio}
              onChange={(event) => setMunicipio(event.target.value)}
            />
          </div>
          <div className="form-group">
            <label htmlFor="uf">UF:</label>
            <input
              type="text"
              className="form-control"
              id="uf"
              placeholder="Digite o UF"
              value={uf}
              onChange={(event) => setUf(event.target.value)}
            />
          </div>
          <div className="form-group">
            <label htmlFor="status">Status:</label>
            <select
              className="form-control"
              id="status"
              value={status}
              onChange={(event) => setStatus(event.target.value)}
            >
              <option value="">Selecione...</option>
              <option value="A">Ativo</option>
              <option value="I">Inativo</option>
            </select>
          </div>
          <button type="submit" className="btn btn-primary">
            Enviar
          </button>
      </form>
    </div>
  );
};

export default CadastroClinica;



  