import React, { useState } from 'react';

const CadastroAnimal = () => {
    const [nomeAnimal, setNomeAnimal] = useState('');
    const [raca, setRaca] = useState('');
    const [dataNascimento, setDataNascimento] = useState('');
    const [porte, setPorte] = useState('');
    const [cor, setCor] = useState('');
    const [responsavel, setResponsavel] = useState('');
    const [status, setStatus] = useState('');

    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();

        // Lógica para manipular os dados do formulário
        const formData = {
            nomeAnimal,
            raca,
            dataNascimento,
            porte,
            cor,
            responsavel,
            status
        };

        console.log('Dados do formulário:', formData);

        // Aqui você pode realizar a lógica para enviar os dados do formulário
        // Por exemplo, você pode fazer uma requisição HTTP para enviar os dados para um servidor

        // Exemplo de envio assíncrono usando fetch:
        fetch('https://exemplo.com/api/clinica', {
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
                setNomeAnimal('');
                setRaca('');
                setDataNascimento('');
                setPorte('');
                setCor('');
                setResponsavel('');
                setStatus('');
            })
            .catch(error => {
                // Aqui você pode tratar o erro caso ocorra algum problema durante o envio do formulário
                console.error('Erro ao enviar formulário:', error);
            });
    };

    return (
        <div className="container">
            <h1>Cadastro Animal</h1>
            <br />
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="nomeAnimal">Nome do animal:</label>
                    <input
                        type="text"
                        className="form-control"
                        id="nomeAnimal"
                        placeholder="Digite o nome do animal"
                        value={nomeAnimal}
                        onChange={(e) => setNomeAnimal(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="raca">Raça:</label>
                    <input
                        type="text"
                        className="form-control"
                        id="raca"
                        placeholder="Digite a raça do animal"
                        value={raca}
                        onChange={(e) => setRaca(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="dataNascimento">Data de nascimento:</label>
                    <input
                        type="date"
                        className="form-control"
                        id="dataNascimento"
                        value={dataNascimento}
                        onChange={(e) => setDataNascimento(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="porte">Porte:</label>
                    <select
                        className="form-control"
                        id="porte"
                        value={porte}
                        onChange={(e) => setPorte(e.target.value)}
                    >
                        <option value="pequeno">Pequeno</option>
                        <option value="médio">Médio</option>
                        <option value="grande">Grande</option>
                    </select>
                </div>
                <div className="form-group">
                    <label htmlFor="cor">Cor:</label>
                    <input
                        type="text"
                        className="form-control"
                        id="cor"
                        placeholder="Digite a cor do animal"
                        value={cor}
                        onChange={(e) => setCor(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="responsavel">Responsável:</label>
                    <input
                        type="text"
                        className="form-control"
                        id="responsavel"
                        placeholder="Digite o nome do responsável"
                        value={responsavel}
                        onChange={(e) => setResponsavel(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="status">Status:</label>
                    <input
                        type="text"
                        className="form-control"
                        id="status"
                        placeholder="Digite o status do animal"
                        value={status}
                        onChange={(e) => setStatus(e.target.value)}
                    />
                </div>
                <button type="submit" className="btn btn-primary">
                    Enviar
                </button>
            </form>
        </div>
    );
};

export default CadastroAnimal;
