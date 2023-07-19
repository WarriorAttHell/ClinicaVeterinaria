import { ListItemButton, ListItemIcon } from '@mui/material';
import { RouteType } from '../../routes/configs'
import { Link } from 'react-router-dom';
import colorConfigs from '../../configs/colorConfigs';
import { RootState } from '../../redux/store';
import { useSelector } from 'react-redux';

type Props = {
    item: RouteType;
}

const SidebarItem = ({ item }: Props) => {
    const { appState } = useSelector((state: RootState) => state.appState)

    return (
        item.SidebarProps && item.path ? (
            <ListItemButton
                component={Link}
                to={item.path}
                sx={{
                    "&: hover":{
                        backgroundColor: colorConfigs.sidebar.hoverBg
                    },
                    backgroundColor: appState === item.state ? colorConfigs.sidebar.activeBg
                    : "unset",
                    paddingY: "12px",
                    paddingX: "24px"
                }}
            >
                <ListItemIcon sx={{
                    color: colorConfigs.sidebar.color
                }}>
                    {item.SidebarProps.icon && item.SidebarProps.icon}
                </ListItemIcon>
                {item.SidebarProps.displaytext}
            </ListItemButton>
        ) : null
    );
};

export default SidebarItem;