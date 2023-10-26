/*
 * Copyright 2023 Ant Group CO., Ltd.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
 * in compliance with the License. You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software distributed under the License
 * is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
 * or implied.
 */

package com.antgroup.openspg.api.http.server.openapi;

import com.antgroup.openspg.api.facade.dto.common.request.ProjectCreateRequest;
import com.antgroup.openspg.api.facade.dto.common.request.ProjectQueryRequest;
import com.antgroup.openspg.api.http.server.BaseController;
import com.antgroup.openspg.api.http.server.HttpBizCallback;
import com.antgroup.openspg.api.http.server.HttpBizTemplate;
import com.antgroup.openspg.biz.common.ProjectManager;
import com.antgroup.openspg.common.model.project.Project;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;


@Controller
@RequestMapping("/public/v1/project")
public class ProjectController extends BaseController {

    @Autowired
    private ProjectManager projectManager;

    @RequestMapping(method = RequestMethod.POST)
    public ResponseEntity<Object> create(@RequestBody ProjectCreateRequest request) {
        return HttpBizTemplate.execute(new HttpBizCallback<Project>() {
            @Override
            public void check() {
            }

            @Override
            public Project action() {
                return projectManager.create(request);
            }
        });
    }

    @RequestMapping(method = RequestMethod.GET)
    public ResponseEntity<Object> query(
        @RequestParam(required = false) Long tenantId,
        @RequestParam(required = false) Long projectId) {
        return HttpBizTemplate.execute(new HttpBizCallback<List<Project>>() {
            @Override
            public void check() {
            }

            @Override
            public List<Project> action() {
                ProjectQueryRequest request = new ProjectQueryRequest();
                request.setTenantId(tenantId);
                request.setProjectId(projectId);
                return projectManager.query(request);
            }
        });
    }
}
