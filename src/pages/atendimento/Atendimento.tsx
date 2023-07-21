import React, { useState } from 'react';
import axios from 'axios';

const AtendimentoFormulario: React.FC = () => {
    const [id_clinica, setIdClinica] = useState<number>();
    const [id_cliente, setIdCliente] = useState<number>();
    const [id_animal, setIdAnimal] = useState<number>();
    const [id_medico, setIdMedico] = useState<number>();
    const [categoria_atendimento, setCategoriaAtendimento] = useState<string>('1');
    const [titulo_atendimento, setTituloAtendimento] = useState<string>('');
    const [descricao_atendimento, setDescricaoAtendimento] = useState<string>('');
    const [urgencia, setUrgencia] = useState<string>('1');
    const [status_atendimento, setStatusAtendimento] = useState<string>('1');
    const [status_pagamento, setStatusPagamento] = useState<string>('1');
    const [vacinas, setVacinas] = useState<number[]>([]);
    const [data_inicio, setDataInicio] = useState<string>('');
    const [data_encerramento, setDataEncerramento] = useState<string>('');
    const [data_pagamento, setDataPagamento] = useState<string>('');

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();

        const formData = {
            id_clinica,
            id_cliente,
            id_animal,
            id_medico,
            categoria_atendimento,
            titulo_atendimento,
            descricao_atendimento,
            urgencia,
            status_atendimento,
            status_pagamento,
            vacinas,
            data_inicio,
            data_encerramento,
            data_pagamento,
        };

        try {
            const response = await axios.post(
                'https://veterinaria.offcurve.com.br/api/v1/atendimento/add_atendimento/',
                formData
            );
            console.log('Resposta do servidor:', response.data);

            // Limpar os campos do formulário após o envio bem-sucedido
            setIdClinica(undefined);
            setIdCliente(undefined);
            setIdAnimal(undefined);
            setIdMedico(undefined);
            setCategoriaAtendimento('1');
            setTituloAtendimento('');
            setDescricaoAtendimento('');
            setUrgencia('1');
            setStatusAtendimento('1');
            setStatusPagamento('1');
            setVacinas([]);
            setDataInicio('');
            setDataEncerramento('');
            setDataPagamento('');
        } catch (error) {
            console.error('Erro ao enviar formulário:', error);
        }
    };

    return (
        <div className="container">
            <h1>Cadastro de Atendimento</h1>
            <br />
            <form onSubmit={handleSubmit}>
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
                    <label htmlFor="idCliente">ID do Cliente:</label>
                    <input
                        type="number"
                        className="form-control"
                        id="idCliente"
                        placeholder="Digite o ID do cliente"
                        value={id_cliente}
                        onChange={(e) => setIdCliente(Number(e.target.value))}
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="idAnimal">ID do Animal:</label>
                    <input
                        type="number"
                        className="form-control"
                        id="idAnimal"
                        placeholder="Digite o ID do animal"
                        value={id_animal}
                        onChange={(e) => setIdAnimal(Number(e.target.value))}
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="idMedico">ID do Médico:</label>
                    <input
                        type="number"
                        className="form-control"
                        id="idMedico"
                        placeholder="Digite o ID do médico"
                        value={id_medico}
                        onChange={(e) => setIdMedico(Number(e.target.value))}
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="categoriaAtendimento">Categoria de Atendimento:</label>
                    <select
                        className="form-control"
                        id="categoriaAtendimento"
                        value={categoria_atendimento}
                        onChange={(e) => setCategoriaAtendimento(e.target.value)}
                    >
                        <option value="1">PetShop</option>
                        <option value="2">Atendimento Médico</option>
                        <option value="3">Intervenção Cirúrgica</option>
                    </select>
                </div>

                <div className="form-group">
                    <label htmlFor="tituloAtendimento">Título do Atendimento:</label>
                    <input
                        type="text"
                        className="form-control"
                        id="tituloAtendimento"
                        placeholder="Digite o título do atendimento"
                        value={titulo_atendimento}
                        onChange={(e) => setTituloAtendimento(e.target.value)}
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="descricaoAtendimento">Descrição do Atendimento:</label>
                    <textarea
                        className="form-control"
                        id="descricaoAtendimento"
                        rows={4}
                        placeholder="Digite a descrição do atendimento"
                        value={descricao_atendimento}
                        onChange={(e) => setDescricaoAtendimento(e.target.value)}
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="urgencia">Urgência:</label>
                    <select
                        className="form-control"
                        id="urgencia"
                        value={urgencia}
                        onChange={(e) => setUrgencia(e.target.value)}
                    >
                        <option value="1">Baixa</option>
                        <option value="2">Média</option>
                        <option value="3">Alta</option>
                        <option value="4">Urgente</option>
                    </select>
                </div>

                <div className="form-group">
                    <label htmlFor="statusAtendimento">Status do Atendimento:</label>
                    <select
                        className="form-control"
                        id="statusAtendimento"
                        value={status_atendimento}
                        onChange={(e) => setStatusAtendimento(e.target.value)}
                    >
                        <option value="1">Aguardando Atendimento</option>
                        <option value="2">Em Atendimento</option>
                        <option value="3">Em Espera</option>
                        <option value="4">Finalizado</option>
                    </select>
                </div>

                <div className="form-group">
                    <label htmlFor="statusPagamento">Status do Pagamento:</label>
                    <select
                        className="form-control"
                        id="statusPagamento"
                        value={status_pagamento}
                        onChange={(e) => setStatusPagamento(e.target.value)}
                    >
                        <option value="1">Aguardando Pagamento</option>
                        <option value="2">Pagamento Realizado</option>
                    </select>
                </div>

                <div className="form-group">
                    <label htmlFor="vacinas">Vacinas:</label>
                    <input
                        type="text"
                        className="form-control"
                        id="vacinas"
                        placeholder="Digite as vacinas (separadas por vírgula)"
                        value={vacinas.join(',')}
                        onChange={(e) => setVacinas(e.target.value.split(',').map((v) => Number(v.trim())))}
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="dataInicio">Data de Início:</label>
                    <input
                        type="datetime-local"
                        className="form-control"
                        id="dataInicio"
                        value={data_inicio}
                        onChange={(e) => setDataInicio(e.target.value)}
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="dataEncerramento">Data de Encerramento:</label>
                    <input
                        type="datetime-local"
                        className="form-control"
                        id="dataEncerramento"
                        value={data_encerramento}
                        onChange={(e) => setDataEncerramento(e.target.value)}
                    />
                </div>

                <div className="form-group">
                    <label htmlFor="dataPagamento">Data de Pagamento:</label>
                    <input
                        type="datetime-local"
                        className="form-control"
                        id="dataPagamento"
                        value={data_pagamento}
                        onChange={(e) => setDataPagamento(e.target.value)}
                    />
                </div>

                <button type="submit" className="btn btn-primary">
                    Enviar
                </button>
            </form>
        </div>
    );
};

export default AtendimentoFormulario;
