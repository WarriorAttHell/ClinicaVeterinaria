import React, { useState } from 'react';
import axios from 'axios';

const CadastroFormaPagamento = () => {
    const [nome_forma_pagamento, setNomeFormaPagamento] = useState('');
    const [dados_integracao, setDadosIntegracao] = useState('AA');
    const [id_clinica, setIdClinica] = useState(2);
    const [status, setStatus] = useState('');

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();

        const formData = {
            nome_forma_pagamento,
            dados_integracao,
            id_clinica,
            status,
        };

        try {
            const response = await axios.post(
                'https://veterinaria.offcurve.com.br/api/v1/forma_pagamento/add_forma_pagamento/',
                formData
            );
            console.log('Resposta do servidor:', response.data);

            // Limpar os campos do formulário após o envio bem-sucedido
            setNomeFormaPagamento('');
            setDadosIntegracao('');
            setIdClinica(2);
            setStatus('');
        } catch (error) {
            console.error('Erro ao enviar formulário:', error);
        }
    };

    return (
        <div className="container">
            <h1>Cadastro de Forma de Pagamento</h1>
            <br />
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="nomeFormaPagamento">Nome da Forma de Pagamento:</label>
                    <input
                        type="text"
                        className="form-control"
                        id="nomeFormaPagamento"
                        placeholder="Digite o nome da forma de pagamento"
                        value={nome_forma_pagamento}
                        onChange={(e) => setNomeFormaPagamento(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="dadosIntegracao">Dados de Integração:</label>
                    <input
                        type="text"
                        className="form-control"
                        id="dadosIntegracao"
                        placeholder="Digite os dados de integração"
                        value={dados_integracao}
                        onChange={(e) => setDadosIntegracao(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="idClinica">ID da Clínica:</label>
                    <input
                        type="number"
                        className="form-control"
                        id="idClinica"
                        placeholder="Digite o ID da clínica"
                        value={id_clinica}
                        onChange={(e) => setIdClinica(Number(e.target.value))}
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

export default CadastroFormaPagamento;