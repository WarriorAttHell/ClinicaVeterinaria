import React, { useState } from 'react';

const Formulario: React.FC = () => {
    const [animalType, setAnimalType] = useState('');
    const [status, setStatus] = useState('');

    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();
        // Lógica para manipular os dados do formulário
        console.log('Tipo de Animal:', animalType);
        console.log('Status:', status);
    };

    return (
        <div className="container">
            <h1>Cadastro Tipo</h1>
            <br/>
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="animalType">Tipo de Animal:</label>
                    <select
                        className="form-control"
                        id="animalType"
                        value={animalType}
                        onChange={(event) => setAnimalType(event.target.value)}
                    >
                        <option value="">Selecione...</option>
                        <option value="Cachorro">Cachorro</option>
                        <option value="Gato">Gato</option>
                        <option value="Outro">Outro</option>
                    </select>
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
                        <option value="Ativo">Ativo</option>
                        <option value="Inativo">Inativo</option>
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
