// ListaClinicas.tsx

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom'; // Importe o useNavigate

interface Clinica {
    id_clinica: number; // Campo correto para o ID da clínica
    nome_clinica: string; // Campo correto para o nome da clínica
    status: string;
}

const ListaClinicas = () => {
    const navigate = useNavigate(); // Obtenha a função navigate
    const [clinicas, setClinicas] = useState<Clinica[]>([]);

    const getClinicasFromAPI = async () => {
        try {
            const response = await axios.get<Clinica[]>('http://veterinaria.offcurve.com.br/api/v1/clinica/listar_clinicas/');
            setClinicas(response.data);
        } catch (error) {
            console.error('Erro ao obter as clínicas:', error);
        }
    };

    useEffect(() => {
        getClinicasFromAPI();
    }, []);

    return (
        <div className="container">
            <h1>Lista de Clínicas</h1>
            <button className="btn btn-primary" onClick={() => navigate('/cadastro-clinica')}>
                Cadastrar Clínica
            </button>
            <table className="table mt-3">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nome</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {clinicas.map((clinica) => (
                        <tr key={clinica.id_clinica}>
                            <td>{clinica.id_clinica}</td>
                            <td>{clinica.nome_clinica}</td>
                            <td>{clinica.status}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ListaClinicas;
