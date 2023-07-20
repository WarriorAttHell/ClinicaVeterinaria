// routes.tsx
import React from 'react';
import { Route } from 'react-router-dom';
import PageWrapper from '../components/layout/PageWrapper';
import appRoutes from './appRoutes';
import { RouteType } from './configs';

const generateRoute = (routes: RouteType[]): React.ReactNode => {
    return routes.map((route, index) =>
        route.index ? (
            <Route
                index
                path={route.path}
                element={
                    <PageWrapper state={route.state}>
                        {route.elemnts}
                    </PageWrapper>
                }
                key={index}
            />
        ) : (
            <Route
                path={route.path}
                element={
                    <PageWrapper state={route.child ? undefined : route.state}>
                        {route.elemnts}
                    </PageWrapper>
                }
                key={index}
            >
                {route.child && generateRoute(route.child)}
            </Route>
        )
    );
};

export const routes: React.ReactNode = (
    <>
        {generateRoute(appRoutes)}
    </>
);
