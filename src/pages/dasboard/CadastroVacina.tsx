import React, { useState } from 'react';
import axios from 'axios';

const CadastroVacina = () => {
    const [id_clinica, setIdClinica] = useState('');
    const [nome_vacina, setNomeVacina] = useState('');
    const [descricao, setDescricao] = useState('');
    const [status, setStatus] = useState('');

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();

        // Lógica para manipular os dados do formulário
        const formData = {
            id_clinica,
            nome_vacina,
            descricao,
            status,
        };

        console.log('Dados do formulário:', formData);

        try {
            // Aqui você pode realizar a lógica para enviar os dados do formulário
            // Por exemplo, fazer a chamada HTTP para enviar os dados para a API
            const response = await axios.post(
                'https://veterinaria.offcurve.com.br/api/v1/vacina/add_vacina/', // Substitua pela URL correta da API de vacinas
                formData
            );
            console.log('Resposta do servidor:', response.data);

            // Limpar os campos do formulário após o envio bem-sucedido
            setIdClinica('');
            setNomeVacina('');
            setDescricao('');
            setStatus('');
        } catch (error) {
            // Tratar o erro caso ocorra algum problema durante o envio do formulário
            console.error('Erro ao enviar formulário:', error);
        }
    };

    return (
        <div className="container">
            <h1>Cadastro de Vacina</h1>
            <br />
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="idClinica">ID da Clínica:</label>
                    <input
                        type="text"
                        className="form-control"
                        id="idClinica"
                        placeholder="Digite o ID da Clínica"
                        value={id_clinica}
                        onChange={(e) => setIdClinica(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="nomeVacina">Nome da Vacina:</label>
                    <input
                        type="text"
                        className="form-control"
                        id="nomeVacina"
                        placeholder="Digite o nome da vacina"
                        value={nome_vacina}
                        onChange={(e) => setNomeVacina(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="descricao">Descrição:</label>
                    <textarea
                        className="form-control"
                        id="descricao"
                        placeholder="Digite a descrição da vacina"
                        value={descricao}
                        onChange={(e) => setDescricao(e.target.value)}
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

export default CadastroVacina;
