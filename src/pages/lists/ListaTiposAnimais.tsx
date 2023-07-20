import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

// Interface para representar os dados dos tipos de animais
interface TipoAnimal {
    id_tipo_animal: number;
    nome_tipo_animal: string;
    status: string;
}

const ListaTiposAnimais = () => {
    const [tiposAnimais, setTiposAnimais] = useState<TipoAnimal[]>([]);

    const getTiposAnimaisFromAPI = async () => {
        try {
            const response = await axios.get<TipoAnimal[]>(
                'https://veterinaria.offcurve.com.br/api/v1/tipo_animal/listar_tipo_animais/'
            );
            setTiposAnimais(response.data);
        } catch (error) {
            console.error('Erro ao obter os tipos de animais:', error);
        }
    };

    useEffect(() => {
        getTiposAnimaisFromAPI();
    }, []);

    return (
        <div className="container">
            <h1>Lista de Tipos de Animais</h1>

            <Link to="/dashboard/cadastrar-tipo-animal" className="btn btn-primary mb-3">
                Cadastrar Tipo de Animal
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
                    {tiposAnimais.map((tipoAnimal) => (
                        <tr key={tipoAnimal.id_tipo_animal}>
                            <td>{tipoAnimal.id_tipo_animal}</td>
                            <td>{tipoAnimal.nome_tipo_animal}</td>
                            <td>{tipoAnimal.status}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ListaTiposAnimais;
