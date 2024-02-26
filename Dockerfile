FROM girder/girder as base

WORKDIR /app/girder

ENV GIRDER_CONFIG /app/girder/config/girder.cfg
COPY girder.dev.cfg ${GIRDER_CONFIG}

COPY plugin /app/girder/plugin
RUN pip install -e ./plugin --config-settings editable_mode=compat

RUN girder build

ENTRYPOINT ["girder", "serve", "--dev"]

