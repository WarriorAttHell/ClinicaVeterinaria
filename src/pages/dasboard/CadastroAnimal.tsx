import React, { useState } from 'react';
import axios from 'axios'; // Importe o axios para fazer a chamada HTTP

const CadastroAnimal = () => {
    const [nome_animal, setNomeAnimal] = useState('');
    const [raca_animal, setRacaAnimal] = useState('');
    const [data_nascimento, setDataNascimento] = useState('');
    const [porte, setPorte] = useState('');
    const [cor, setCor] = useState('');
    const [id_responsavel, setIdResponsavel] = useState('');
    const [status, setStatus] = useState('');

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();

        // Lógica para manipular os dados do formulário
        const formData = {
            nome_animal,
            raca_animal,
            data_nascimento,
            porte,
            cor,
            id_responsavel,
            status,
        };

        console.log('Dados do formulário:', formData);

        try {
            // Aqui você pode realizar a lógica para enviar os dados do formulário
            // Por exemplo, fazer a chamada HTTP para enviar os dados para a API
            const response = await axios.post(
                'https://veterinaria.offcurve.com.br/api/v1/animal/add_animal/',
                formData
            );
            console.log('Resposta do servidor:', response.data);

            // Limpar os campos do formulário após o envio bem-sucedido
            setNomeAnimal('');
            setRacaAnimal('');
            setDataNascimento('');
            setPorte('');
            setCor('');
            setIdResponsavel('');
            setStatus('');
        } catch (error) {
            // Tratar o erro caso ocorra algum problema durante o envio do formulário
            console.error('Erro ao enviar formulário:', error);
        }
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
                        value={nome_animal}
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
                        value={raca_animal}
                        onChange={(e) => setRacaAnimal(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="dataNascimento">Data de nascimento:</label>
                    <input
                        type="date"
                        className="form-control"
                        id="dataNascimento"
                        value={data_nascimento}
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
                        value={id_responsavel}
                        onChange={(e) => setIdResponsavel(e.target.value)}
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
