/** @odoo-module */

import {ProjectTaskMapArchParser} from "./project_task_map_arch_parser.esm";
import {ProjectTaskMapController} from "./project_task_map_controller.esm";
import {ProjectTaskMapModel} from "./project_task_map_model.esm";
import {ProjectTaskMapRenderer} from "./project_task_map_renderer.esm";
import {registry} from "@web/core/registry";

export const ProjectTaskMapView = {
    type: "ProjectTaskMapView",
    display_name: "Map",
    icon: "fa fa-map",
    multiRecord: true,
    Controller: ProjectTaskMapController,
    ArchParser: ProjectTaskMapArchParser,
    Model: ProjectTaskMapModel,
    Renderer: ProjectTaskMapRenderer,

    props(genericProps, view) {
        const {ArchParser} = view;
        const {arch} = genericProps;
        const archInfo = new ArchParser().parse(arch);

        return {
            ...genericProps,
            Model: view.Model,
            Renderer: view.Renderer,
            archInfo,
        };
    },
};

registry.category("views").add("ProjectTaskMapView", ProjectTaskMapView);
