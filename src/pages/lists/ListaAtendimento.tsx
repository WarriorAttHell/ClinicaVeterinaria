import React, { useEffect, useState } from 'react';
import axios from 'axios';

const AtendimentoListagem: React.FC = () => {
    const [atendimentos, setAtendimentos] = useState([]);

    useEffect(() => {
        fetchAtendimentos();
    }, []);

    const fetchAtendimentos = async () => {
        try {
            const response = await axios.get('https://veterinaria.offcurve.com.br/api/v1/atendimento/listar_atendimentos/');
            setAtendimentos(response.data);
        } catch (error) {
            console.error('Erro ao obter a lista de atendimentos:', error);
        }
    };

    return (
        <div className="container">
            <h1>Lista de Atendimentos</h1>
            <table className="table mt-3">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Clínica</th>
                        <th>Cliente</th>
                        <th>Animal</th>
                        <th>Médico</th>
                        <th>Categoria</th>
                        <th>Título</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {atendimentos.map((atendimento: any) => (
                        <tr key={atendimento.id_atendimento}>
                            <td>{atendimento.id_atendimento}</td>
                            <td>{atendimento.id_clinica}</td>
                            <td>{atendimento.id_cliente}</td>
                            <td>{atendimento.id_animal}</td>
                            <td>{atendimento.id_medico}</td>
                            <td>{atendimento.categoria_atendimento}</td>
                            <td>{atendimento.titulo_atendimento}</td>
                            <td>{atendimento.status_atendimento}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default AtendimentoListagem;
