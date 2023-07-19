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

const appRoutes: RouteType[] = [
    {
        index: true,
        elemnts: <HomePage/>,
        state: "home"
    },
    {
        path: "/dashboard",
        elemnts: <DashboardPageLayout/>,
        state: "dashboard",
        SidebarProps: {
            displaytext: "Cadastro",
            icon: <DashboardOutlinedIcon/>
        },
        child: [
            {
                index: true,
                elemnts: <DashboardIndex />,
                state: "dashboard.index"
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
                path: "/dashboard/racaanimal",
                elemnts: <RacaAnimal />,
                state: "dashboard.racaanimal",
                SidebarProps: {
                    displaytext: "Raça Animal"
                }
            },
            {
                path: "/dashboard/tipoanimal",
                elemnts: <TipoAnimal />,
                state: "dashboard.tipoanimal",
                SidebarProps: {
                    displaytext: "Tipo Animal"
                }
            },
            {
                path: "/dashboard/cadastroclinica",
                elemnts: <CadastroClinica />,
                state: "dashboard.cadstroclinica",
                SidebarProps: {
                    displaytext: "Clinica"
                }
            }
        ]
    },
    {
        path: "/changelog",
        elemnts: <Perfil />,
        state: "changelog",
        SidebarProps: {
            displaytext: "Perfil",
            icon: <ListOutlinedIcon />
        }
    }
    
    
];

export default appRoutes