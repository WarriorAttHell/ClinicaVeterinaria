import RacaAnimal from "../pages/dasboard/RacaAnimal";
import DashboardIndex from "../pages/dasboard/DashboardIndex";
import DashboardPageLayout from "../pages/dasboard/DashboardPageLayout";
import CadastroAnimal from "../pages/dasboard/CadastroAnimal";
import TipoAnimal from "../pages/dasboard/TipoAnimal";
import HomePage from "../pages/home/HomePage";
import { RouteType } from "./configs";
import DashboardOutlinedIcon from '@mui/icons-material/DashboardOutlined';
import ListOutlinedIcon from '@mui/icons-material/ListOutlined';
import Perfil from "../pages/changelog/Perfil";
import CadastroClinica from "../pages/dasboard/CadastroClinica";
import ListaClinicas from "../pages/lists/ListaClinicas";
import ListaAnimais from "../pages/lists/ListaAnimais";
import ListPageLayout from "../pages/lists/ListPageLayout";
import ListaTiposAnimais from "../pages/lists/ListaTiposAnimais";
import CadastroVacina from "../pages/dasboard/CadastroVacina";
import ListaVacinas from "../pages/lists/ListaVacina";
import CadastroFormaPagamento from "../pages/dasboard/CadastroFormaPagamento";
import Page from "../pages/atendimento/Page";
import Atendimento from "../pages/atendimento/Atendimento";
import WorkOutlineOutlinedIcon from '@mui/icons-material/WorkOutlineOutlined';


const appRoutes: RouteType[] = [
    {
        index: true,
        elemnts: <HomePage />,
        state: "home"
    },
    {
        path: "/dashboard",
        elemnts: <DashboardPageLayout />,
        state: "dashboard",
        SidebarProps: {
            displaytext: "Cadastro",
            icon: <DashboardOutlinedIcon />
        },
        child: [
            {
                index: true,
                elemnts: <DashboardIndex />,
                state: "dashboard.index"
            },
            {
                path: "/dashboard/cadastrar-tipo-animal",
                elemnts: <TipoAnimal />,
                state: "dashboard.tipoanimal",
                SidebarProps: {
                    displaytext: "Tipo Animal"
                }
            },
            {
                path: "/dashboard/racaanimal",
                elemnts: <RacaAnimal />,
                state: "dashboard.racaanimal",
                SidebarProps: {
                    displaytext: "Raça Animal"
                }
            },
            {
                path: "/dashboard/animal",
                elemnts: <CadastroAnimal />,
                state: "dashboard.cadastroanimal",
                SidebarProps: {
                    displaytext: "Animal"
                }
            },
            {
                path: "/dashboard/cadastroclinica",
                elemnts: <CadastroClinica />,
                state: "dashboard.cadstroclinica",
                SidebarProps: {
                    displaytext: "Clinica"
                }
            },
            {
                path: "/dashboard/cadastrovacina",
                elemnts: <CadastroVacina />,
                state: "dashboard.cadastrovacina",
                SidebarProps: {
                    displaytext: "Vacinas"
                }
            },
            {
                path: "/dashboard/cadastroformapagaemnto",
                elemnts: <CadastroFormaPagamento />,
                state: "dashboard.cadastroformapagamento",
                SidebarProps: {
                    displaytext: "Forma de Pagamento"
                }
            },
            {
                path: "/dashboard/perfil",
                elemnts: <Perfil />,
                state: "dashboard.perfil",
                SidebarProps: {
                    displaytext: "Perfil"
                }
            }
        ]
    },
    {
        path: "/list",
        elemnts: <ListPageLayout />,
        state: "lists",
        SidebarProps: {
            displaytext: "Listagens",
            icon: <ListOutlinedIcon />
        },
        child: [
            {
                path: "/list/listclinica",
                elemnts: <ListaClinicas />,
                state: "lists.listaclinica",
                SidebarProps: {
                    displaytext: "Listagem de Clinicas"
                }
            },
            {
                path: "/list/listaanimal",
                elemnts: <ListaAnimais />,
                state: "lists.listaanimal",
                SidebarProps: {
                displaytext: "Listagem de Animais",
                }
            },
            {
                path: "/list/listtipoanimal",
                elemnts: <ListaTiposAnimais />,
                state: "lists.listatipoanimal",
                SidebarProps: {
                displaytext: "Listagem dos Tipos de Animais",
                }
            },
            {
                path: "/list/listvacina",
                elemnts: <ListaVacinas />,
                state: "lists.listavacina",
                SidebarProps: {
                displaytext: "Listagem das vacinas",
                }
            },
            
        ]
    },
    {
        path: "/atendimento",
        elemnts: <Page />,
        state: "page",
        SidebarProps: {
            displaytext: "Atendimento",
            icon: <WorkOutlineOutlinedIcon />
        },
        child: [
            {
                path: "/atendimento/atendimentos",
                elemnts: <Atendimento />,
                state: "atendimento.atendimentos",
                SidebarProps: {
                    displaytext: "Atendimentos"
                }
            },
        ]
    }


];

export default appRoutes