
RUN addgroup --system nonroot && adduser --system --no-create-home --disabled-password --group nonroot

USER nonroot