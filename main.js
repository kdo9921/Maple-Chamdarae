function init() {
    document.getElementById('level').innerHTML = data.level;
    document.getElementById('union_tier').innerHTML = data.union_tier;
    document.getElementById('union_level').innerHTML = "(" + data.union_level + ")";
    document.getElementById('rank_world').innerHTML = data.rank_world;
    document.getElementById('rank_world_job').innerHTML = data.rank_world_job;
    document.getElementById('rank_job').innerHTML = data.rank_job;
    document.getElementById('mureung_floor').innerHTML = data.mureung_floor + "층";
    document.getElementById('mureung_time').innerHTML = "(" + data.mureung_time + ")";
    document.getElementById('popular').innerHTML = data.popular; 
}