import React, { useState } from 'react';

const FormularioAnimais = () => {
    const [raca, setRaca] = useState('');
    const [tipoAnimal, setTipoAnimal] = useState('');
    const [status, setStatus] = useState('Ativo');

    const handleSubmit = (event: React.FormEvent) => {
        event.preventDefault();

        // Lógica para manipular os dados do formulário
        const formData = {
            raca,
            tipoAnimal,
            status
        };

        console.log('Dados do formulário:', formData);

        // Aqui você pode realizar a lógica para enviar os dados do formulário
        // Por exemplo, você pode fazer uma requisição HTTP para enviar os dados para um servidor

        // Exemplo de envio assíncrono usando fetch:
        fetch('https://exemplo.com/api/animais', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        })
            .then(response => response.json())
            .then(data => {
                // Aqui você pode tratar a resposta do servidor após o envio do formulário
                console.log('Resposta do servidor:', data);

                // Limpar os campos do formulário após o envio bem-sucedido
                setRaca('');
                setTipoAnimal('');
                setStatus('Ativo');
            })
            .catch(error => {
                // Aqui você pode tratar o erro caso ocorra algum problema durante o envio do formulário
                console.error('Erro ao enviar formulário:', error);
            });
    };

    return (
        <div className="container">
            <h1>Cadastro Raça</h1>
            <br />
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="raca">Raça:</label>
                    <input
                        type="text"
                        className="form-control"
                        id="raca"
                        placeholder="Digite a raça do animal"
                        value={raca}
                        onChange={(event) => setRaca(event.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="tipoAnimal">Tipo de Animal:</label>
                    <input
                        type="text"
                        className="form-control"
                        id="tipoAnimal"
                        placeholder="Digite o tipo de animal"
                        value={tipoAnimal}
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

export default FormularioAnimais;
