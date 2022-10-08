import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";

import { Home } from "./pages/home";
import { App } from "./pages/app";
import { Demo } from "./pages/demo";
import { Sitedetail } from "./pages/sitedetail";
import injectContext from "./store/appContext";

import { Navbar } from "./component/navbar";
import { Footer } from "./component/footer";
import Error404 from "./pages/Error404";
import Modalbox from "./component/modal";
import Dashboard from "./pages/dashboard";
import { FormNewValla } from "./pages/form_new_valla";
import { FormUpdateValla } from "./pages/form_update_valla";

//create your first component
const Layout = () => {
  //the basename is used when your project is published in a subdirectory and not in the root of the domain
  // you can set the basename on the .env file located at the root of this project, E.g: BASENAME=/react-hello-webapp/
  const basename = process.env.BASENAME || "";

  return (
    <div className="d-flex flex-column h-100">
      <BrowserRouter basename={basename}>
        <ScrollToTop>
          <Navbar />
          <Switch>
            <Route exact path="/" component={Home} />
            <Route exact path="/demo" component={Demo} />
            <Route exact path="/dashboard" component={Dashboard} />
            <Route exact path="/app" component={App}></Route>
            <Route exact path="/modal" component={Modalbox} />
            <Route exact path="/formNewValla" component={FormNewValla} />
            <Route
              exact
              path="/formUpdateValla/:id"
              component={FormUpdateValla}
            />
            <Route exact path="/sitedetail/:id" component={Sitedetail} />
            <Route path="*" component={Error404} />
          </Switch>
          <Footer />
        </ScrollToTop>
      </BrowserRouter>
    </div>
  );
};

export default injectContext(Layout);
