import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

interface Animal {
    id_animal: number;
    nome_animal: string;
    raca: string;
    data_nascimento: string;
    porte: string;
    cor: string;
    responsavel: string;
    status: string;
}

const ListaAnimais = () => {
    const navigate = useNavigate();
    const [animais, setAnimais] = useState<Animal[]>([]);

    const getAnimaisFromAPI = async () => {
        try {
            const response = await axios.get<Animal[]>('https://veterinaria.offcurve.com.br/api/v1/animal/listar_animais/');
            setAnimais(response.data);
        } catch (error) {
            console.error('Erro ao obter a lista de animais:', error);
        }
    };

    useEffect(() => {
        getAnimaisFromAPI();
    }, []);

    return (
        <div className="container">
            <h1>Lista de Animais</h1>
            <button className="btn btn-primary" onClick={() => navigate('/dashboard/animal')}>
                Cadastrar Animal
            </button>
            <table className="table mt-3">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nome</th>
                        <th>Raça</th>
                        <th>Data de Nascimento</th>
                        <th>Porte</th>
                        <th>Cor</th>
                        <th>Responsável</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {animais.map((animal) => (
                        <tr key={animal.id_animal}>
                            <td>{animal.id_animal}</td>
                            <td>{animal.nome_animal}</td>
                            <td>{animal.raca}</td>
                            <td>{animal.data_nascimento}</td>
                            <td>{animal.porte}</td>
                            <td>{animal.cor}</td>
                            <td>{animal.responsavel}</td>
                            <td>{animal.status}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ListaAnimais;
