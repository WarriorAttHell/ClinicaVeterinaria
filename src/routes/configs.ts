import { ReactNode } from "react"

export type RouteType = {
    elemnts: ReactNode,
    state: string,
    index?: boolean,
    path?: string,
    child?: RouteType[],
    SidebarProps?: {
        displaytext: string,
        icon?: ReactNode
    };
};