import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

interface Vacina {
    id_clinica: number;
    nome_vacina: string;
    descricao: string;
    status: string;
}

const ListaVacinas: React.FC = () => {
    const [vacinas, setVacinas] = useState<Vacina[]>([]);

    useEffect(() => {
        // Fazendo a chamada à API para obter a lista de vacinas
        axios.get<Vacina[]>('https://veterinaria.offcurve.com.br/api/v1/vacina/listar_vacinas/')
            .then(response => {
                // Armazene os dados obtidos na state "vacinas"
                setVacinas(response.data);
            })
            .catch(error => {
                console.error('Erro ao obter a lista de vacinas:', error);
            });
    }, []);

    return (
        <div className="container">
            <h1>Lista de Vacinas</h1>
            <Link to="/dashboard/cadastrovacina" className="btn btn-primary mb-3">
                Cadastrar Vacina
            </Link>
            <table className="table mt-3">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nome</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {vacinas.map(vacina => (
                        <tr key={vacina.id_clinica}>
                            <td>{vacina.id_clinica}</td>
                            <td>{vacina.nome_vacina}</td>
                            <td>{vacina.status}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ListaVacinas;
