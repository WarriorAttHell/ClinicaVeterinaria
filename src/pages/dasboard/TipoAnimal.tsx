import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Formulario: React.FC = () => {
    const navigate = useNavigate();
    const [nome_tipo_animal, setTipoAnimal] = useState('');
    const [status, setStatus] = useState('');

    const handleSubmit = async (event: React.FormEvent) => {
        event.preventDefault();

        const formData = {
            nome_tipo_animal,
            status,
        };

        try {
            // Aqui você pode realizar a lógica para enviar os dados do formulário
            // Por exemplo, você pode fazer uma requisição HTTP para enviar os dados para um servidor

            // Exemplo de envio assíncrono usando axios:
            await axios.post(
                'https://veterinaria.offcurve.com.br/api/v1/tipo_animal/add_tipo_animal/',
                formData
            );

            // Limpar os campos do formulário após o envio bem-sucedido
            setTipoAnimal('');
            setStatus('');

            // Redirecionar para onde desejar após o cadastro
            // Por exemplo, para a lista de tipos de animais
            navigate('/lista-tipos-animais');
        } catch (error) {
            // Aqui você pode tratar o erro caso ocorra algum problema durante o envio do formulário
            console.error('Erro ao enviar formulário:', error);
        }
    };

    return (
        <div className="container">
            <h1>Cadastro Tipo</h1>
            <br />
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="tipoAnimal">Tipo de Animal:</label>
                    <input
                        type="text"
                        className="form-control"
                        id="tipoAnimal"
                        placeholder="Digite o tipo de animal"
                        value={nome_tipo_animal}
                        onChange={(event) => setTipoAnimal(event.target.value)}
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

export default Formulario;
