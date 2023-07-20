import React, { useState } from 'react';

const Perfil = () => {
    const [nome, setNome] = useState('');
    const [endereco, setEndereco] = useState('');
    const [bairro, setBairro] = useState('');
    const [cep, setCep] = useState('');
    const [municipio, setMunicipio] = useState('');
    const [uf, setUf] = useState('');
    const [status, setStatus] = useState('Ativo');
    const [usuario, setUsuario] = useState('');

    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();

        // Lógica para manipular os dados do formulário
        const formData = {
            nome,
            endereco,
            bairro,
            cep,
            municipio,
            uf,
            status,
            usuario
        };

        console.log('Dados do formulário:', formData);

        // Aqui você pode realizar a lógica para enviar os dados do formulário
        // Por exemplo, você pode fazer uma requisição HTTP para enviar os dados para um servidor

        // Exemplo de envio assíncrono usando fetch:
        fetch('https://exemplo.com/api/usuario', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        })
            .then(response => response.json())
            .then(data => {
                // Aqui você pode tratar a resposta do servidor após o envio do formulário
                console.log('Resposta do servidor:', data);

                // Limpar os campos do formulário após o envio bem-sucedido
                setNome('');
                setEndereco('');
                setBairro('');
                setCep('');
                setMunicipio('');
                setUf('');
                setStatus('Ativo');
                setUsuario('');
            })
            .catch(error => {
                // Aqui você pode tratar o erro caso ocorra algum problema durante o envio do formulário
                console.error('Erro ao enviar formulário:', error);
            });
    };

    return (
        <div className="container">
            <h1>Cadastro Usuário</h1>
            <br />
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="nome">Nome:</label>
                    <input
                        type="text"
                        className="form-control"
                        id="nome"
                        placeholder="Digite o nome"
                        value={nome}
                        onChange={(event) => setNome(event.target.value)}
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
                        <option value="A">Ativo</option>
                        <option value="I">Inativo</option>
                    </select>
                </div>
                <div className="form-group">
                    <label htmlFor="usuario">Usuário:</label>
                    <input
                        type="text"
                        className="form-control"
                        id="usuario"
                        placeholder="Digite o usuário"
                        value={usuario}
                        onChange={(event) => setUsuario(event.target.value)}
                    />
                </div>
                <button type="submit" className="btn btn-primary">
                    Enviar
                </button>
            </form>
        </div>
    );
};

export default Perfil;
